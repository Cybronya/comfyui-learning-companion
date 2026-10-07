---
key: comfyui-workflow-templates-json/txt_to_image_to_video.json
name: txt_to_image_to_video
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/txt_to_image_to_video.json
hash: 5f10394fa88508f8
official: true
coverage: 0.866667
learned_at: 2026-10-07 21:36:41
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, CheckpointLoaderSimple, VAEDecode, SVD_img2vid_Conditioning, VideoLinearCFGGuidance, ImageOnlyCheckpointLoader, CreateVideo, KSampler, VAEDecode, PreviewImage, MarkdownNote, SaveVideo]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "svd_xt.safetensors", "denoise": 1, "height": 576, "sampler_name": "uni_pc_bh2", "scheduler": "normal", "seed": 144698910769133, "steps": 15, "width": 1024}
---

# comfyui-workflow-templates-json/txt_to_image_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/txt_to_image_to_video.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SVD_img2vid_Conditioning`
- `VideoLinearCFGGuidance`
- `ImageOnlyCheckpointLoader` ★核心
- `CreateVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `MarkdownNote`
- `SaveVideo`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `144698910769133`
- `steps` = `15`
- `cfg` = `8`
- `sampler_name` = `uni_pc_bh2`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `1024`
- `height` = `576`
- `batch_size` = `1`
- `checkpoint` = `svd_xt.safetensors`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`VAEDecode`、`SVD_img2vid_Conditioning`、`VideoLinearCFGGuidance`、`ImageOnlyCheckpointLoader`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、VideoLinearCFGGuidance、ImageOnlyCheckpointLoader、SVD_img2vid_Conditioning
