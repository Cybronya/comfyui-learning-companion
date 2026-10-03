# Workflow Category Rules

## Purpose

定义 Workflow 自动分类规则。

分类依据：

- 文件路径
- 节点类型
- 模型类型

## Primary Categories

### image_generation

包含：

- CheckpointLoader
- KSampler
- CLIPTextEncode
- VAEDecode

用于 txt2img 等图像生成流程。

### image_editing

包含：

- LoadImage
- VAEEncode
- ControlNet

用于 img2img、inpainting 等。

### upscale

包含：

- UpscaleModelLoader
- ImageUpscale

### video_generation

包含：

- Video
- Animate
- Wan
- HunyuanVideo
- LTX

### animation

包含：

- AnimateDiff
- MotionModule
- VideoCombine

### training

包含：

- Dataset
- Trainer
- LoRA Training

## Model Based Classification

模型信息可以辅助分类：

Wan -> video_generation

SDXL -> image_generation

FLUX -> image_generation + advanced

## Multi Category

允许一个 Workflow 拥有多个分类。

例如：

```
wan_character_animation

[
 video_generation,
 character_animation
]
```

## Unknown

无法判断时保存为：

```
unknown
```

等待人工确认。

## Priority

自动分类为 suggestion。

human_confirmed 优先级最高。