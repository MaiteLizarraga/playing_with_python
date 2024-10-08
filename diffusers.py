# Diffusion models are a type of generative model used in various applications such as image generation, data augmentation, and other tasks in machine learning and artificial intelligence.

!pip install diffusers
from diffusers import DDPMPipeline, DDIMPipeline, PNDMPipeline

model_id = "google/ddpm-cifar10-32"

# load model and scheduler
ddpm = DDPMPipeline.from_pretrained(model_id)  # you can replace DDPMPipeline with DDIMPipeline or PNDMPipeline for faster inference

# run pipeline in inference (sample random noise and denoise)
image = ddpm().images[0]

# save image
image.save("ddpm_generated_image.png")

print(image)