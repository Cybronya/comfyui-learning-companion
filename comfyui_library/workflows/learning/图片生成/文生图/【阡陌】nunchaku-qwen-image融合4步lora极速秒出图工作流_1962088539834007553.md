---
key: 图片生成/文生图/【阡陌】nunchaku-qwen-image融合4步lora极速秒出图工作流_1962088539834007553.json
name: 【阡陌】nunchaku-qwen-image融合4步lora极速秒出图工作流_1962088539834007553
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【阡陌】nunchaku-qwen-image融合4步lora极速秒出图工作流_1962088539834007553.json
hash: 2ceda04c63caee08
coverage: 1
learned_at: 2026-10-10 20:59:32
nodes: [SaveImage, VAEDecode, LoadImage, ModelSamplingAuraFlow, KSampler, EmptyLatentImage, LoraLoaderModelOnly, NunchakuQwenImageDiTLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 248921332779208, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【阡陌】nunchaku-qwen-image融合4步lora极速秒出图工作流_1962088539834007553.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【阡陌】nunchaku-qwen-image融合4步lora极速秒出图工作流_1962088539834007553.json`

## 结构

**节点**（13 个）：
- `SaveImage`
- `VAEDecode`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `KSampler`
- `EmptyLatentImage`
- `LoraLoaderModelOnly`
- `NunchakuQwenImageDiTLoader`
- `UNETLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `CLIPLoader`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `248921332779208`
- `steps` = `4`
- `width` = `768`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`SaveImage`、`VAEDecode`、`LoadImage`、`ModelSamplingAuraFlow`、`KSampler`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`NunchakuQwenImageDiTLoader`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
