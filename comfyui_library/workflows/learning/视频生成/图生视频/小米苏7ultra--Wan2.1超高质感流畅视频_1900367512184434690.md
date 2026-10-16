---
key: 视频生成/图生视频/小米苏7ultra--Wan2.1超高质感流畅视频_1900367512184434690.json
name: 小米苏7ultra--Wan2.1超高质感流畅视频_1900367512184434690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1900367512184434690.json
hash: 3926424d0a90b1a1
coverage: 0.92
learned_at: 2026-10-15 22:29:23
nodes: [PathchSageAttentionKJ, UnetLoaderGGUF, TorchCompileModelWanVideo, ModelSamplingSD3, WanVideoTeaCacheKJ, LoadImage, VHS_VideoCombine, PreviewImage, PreviewImage, VHS_VideoCombine, workflow>CLIP视觉编码, workflow>从批次获取图像, workflow>WanimageToVideo, workflow>获取图像尺寸数量, workflow>图像组合批次, workflow>数学表达式, workflow>采样组, CLIPTextEncode, CLIPTextEncode, workflow>CLIP文本编码器, workflow>整数, workflow>模型加载, workflow>CLIP视觉加载器, Note _O, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/小米苏7ultra--Wan2.1超高质感流畅视频_1900367512184434690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1900367512184434690.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（25 个）：
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `TorchCompileModelWanVideo`
- `ModelSamplingSD3`
- `WanVideoTeaCacheKJ`
- `LoadImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `workflow>CLIP视觉编码`
- `workflow>从批次获取图像`
- `workflow>WanimageToVideo`
- `workflow>获取图像尺寸数量`
- `workflow>图像组合批次`
- `workflow>数学表达式`
- `workflow>采样组`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `workflow>CLIP文本编码器`
- `workflow>整数`
- `workflow>模型加载`
- `workflow>CLIP视觉加载器`
- `Note _O`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`TorchCompileModelWanVideo`、`ModelSamplingSD3`、`WanVideoTeaCacheKJ`、`LoadImage`、`VHS_VideoCombine`、`workflow>CLIP视觉编码`、`workflow>从批次获取图像`、`workflow>WanimageToVideo`、`workflow>获取图像尺寸数量`、`workflow>图像组合批次`、`workflow>数学表达式`、`workflow>采样组`、`CLIPTextEncode`、`workflow>CLIP文本编码器`、`workflow>整数`、`workflow>模型加载`、`workflow>CLIP视觉加载器`、`Note _O`

**用到的条目**：CLIPTextEncode、LoadImage、workflow>采样组、workflow>CLIP视觉编码、workflow>CLIP文本编码器、workflow>CLIP视觉编码、workflow>模型加载、workflow>CLIP视觉加载器
