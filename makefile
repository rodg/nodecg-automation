registry:=registry.digitalocean.com
image_name:=rods-registry/nodecg-base
deploy_name:=rods-registry/nodecg
version?=$(shell find . -type f -exec sha1sum {} + | awk '{print $1}' | sort | sha1sum | cut -c 1-8)

base_image = ${registry}/${image_name}
deploy_image = ${registry}/${deploy_name}

build: 
	docker build -f ./docker/Dockerfile -t ${deploy_image}:${version} .

push: 
	docker push ${deploy_image}:${version}

tag-ci-%: 
	docker tag ${deploy_image}:${version} ${deploy_image}:$*
	docker push ${deploy_image}:$*

publish: build push tag-ci-latest
