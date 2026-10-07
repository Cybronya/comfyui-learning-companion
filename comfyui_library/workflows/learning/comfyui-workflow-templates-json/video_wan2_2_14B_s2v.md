---
key: comfyui-workflow-templates-json/video_wan2_2_14B_s2v.json
name: video_wan2_2_14B_s2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_s2v.json
hash: 9b017cde7f056496
official: true
coverage: 0.596774
learned_at: 2026-10-07 21:37:16
nodes: [CLIPLoader, VAEDecode, CLIPTextEncode, VAELoader, AudioEncoderLoader, WanSoundImageToVideo, ModelSamplingSD3, ImageFromBatch, LatentConcat, LatentCut, CLIPTextEncode, Note, 866cdb67-cb97-4a54-8738-e9ece4f5f25f, PrimitiveInt, CreateVideo, SaveVideo, PrimitiveInt, MarkdownNote, ad3f1d6b-f6de-4f22-abcf-caeed4bf8ce4, AudioEncoderEncode, 92cfa20b-adb6-4f00-8596-f14b534cf926, Note, LoraLoaderModelOnly, PrimitiveInt, PrimitiveFloat, CLIPLoader, VAEDecode, CLIPTextEncode, VAELoader, AudioEncoderLoader, KSampler, WanSoundImageToVideo, ModelSamplingSD3, ImageFromBatch, LatentConcat, LatentCut, CLIPTextEncode, Note, d7670b5a-34e9-40f6-ac84-ec52996e52f3, PrimitiveInt, CreateVideo, PrimitiveInt, MarkdownNote, bdee126d-2d92-4d01-9e74-9118a9d609c5, AudioEncoderEncode, SaveVideo, PrimitiveInt, PrimitiveFloat, MarkdownNote, MarkdownNote, MarkdownNote, 51b3a856-6e10-44f8-94d7-2a92a39c9707, UNETLoader, UNETLoader, Note, MarkdownNote, KSampler, MarkdownNote, LoadAudio, LoadImage, LoadAudio, LoadImage]
patterns: []
missing: [51b3a856-6e10-44f8-94d7-2a92a39c9707, 866cdb67-cb97-4a54-8738-e9ece4f5f25f, 92cfa20b-adb6-4f00-8596-f14b534cf926, ad3f1d6b-f6de-4f22-abcf-caeed4bf8ce4, bdee126d-2d92-4d01-9e74-9118a9d609c5, d7670b5a-34e9-40f6-ac84-ec52996e52f3]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 20, "steps": 10}
discoveries: [次要节点 `51b3a856-6e10-44f8-94d7-2a92a39c9707` 知识库中没有该节点类型的任何知识, 次要节点 `866cdb67-cb97-4a54-8738-e9ece4f5f25f` 知识库中没有该节点类型的任何知识, 次要节点 `92cfa20b-adb6-4f00-8596-f14b534cf926` 知识库中没有该节点类型的任何知识, 次要节点 `ad3f1d6b-f6de-4f22-abcf-caeed4bf8ce4` 知识库中没有该节点类型的任何知识, 次要节点 `bdee126d-2d92-4d01-9e74-9118a9d609c5` 知识库中没有该节点类型的任何知识, 次要节点 `d7670b5a-34e9-40f6-ac84-ec52996e52f3` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_wan2_2_14B_s2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2_2_14B_s2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `AudioEncoderLoader`
- `WanSoundImageToVideo`
- `ModelSamplingSD3`
- `ImageFromBatch`
- `LatentConcat`
- `LatentCut`
- `CLIPTextEncode` ★核心
- `Note`
- `866cdb67-cb97-4a54-8738-e9ece4f5f25f`
- `PrimitiveInt`
- `CreateVideo`
- `SaveVideo`
- `PrimitiveInt`
- `MarkdownNote`
- `ad3f1d6b-f6de-4f22-abcf-caeed4bf8ce4`
- `AudioEncoderEncode`
- `92cfa20b-adb6-4f00-8596-f14b534cf926`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `AudioEncoderLoader`
- `KSampler` ★核心
- `WanSoundImageToVideo`
- `ModelSamplingSD3`
- `ImageFromBatch`
- `LatentConcat`
- `LatentCut`
- `CLIPTextEncode` ★核心
- `Note`
- `d7670b5a-34e9-40f6-ac84-ec52996e52f3`
- `PrimitiveInt`
- `CreateVideo`
- `PrimitiveInt`
- `MarkdownNote`
- `bdee126d-2d92-4d01-9e74-9118a9d609c5`
- `AudioEncoderEncode`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `51b3a856-6e10-44f8-94d7-2a92a39c9707`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `MarkdownNote`
- `KSampler` ★核心
- `MarkdownNote`
- `LoadAudio`
- `LoadImage`
- `LoadAudio`
- `LoadImage`

## 关键参数

- `seed` = `20`
- `steps` = `10`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **60%**（37/62）

**有卡**：`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`AudioEncoderLoader`、`WanSoundImageToVideo`、`ModelSamplingSD3`、`ImageFromBatch`、`LatentConcat`、`LatentCut`、`CreateVideo`、`SaveVideo`、`AudioEncoderEncode`、`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`LoadAudio`、`LoadImage`

**缺卡**（6）：`51b3a856-6e10-44f8-94d7-2a92a39c9707`、`866cdb67-cb97-4a54-8738-e9ece4f5f25f`、`92cfa20b-adb6-4f00-8596-f14b534cf926`、`ad3f1d6b-f6de-4f22-abcf-caeed4bf8ce4`、`bdee126d-2d92-4d01-9e74-9118a9d609c5`、`d7670b5a-34e9-40f6-ac84-ec52996e52f3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `51b3a856-6e10-44f8-94d7-2a92a39c9707` 知识库中没有该节点类型的任何知识
- 次要节点 `866cdb67-cb97-4a54-8738-e9ece4f5f25f` 知识库中没有该节点类型的任何知识
- 次要节点 `92cfa20b-adb6-4f00-8596-f14b534cf926` 知识库中没有该节点类型的任何知识
- 次要节点 `ad3f1d6b-f6de-4f22-abcf-caeed4bf8ce4` 知识库中没有该节点类型的任何知识
- 次要节点 `bdee126d-2d92-4d01-9e74-9118a9d609c5` 知识库中没有该节点类型的任何知识
- 次要节点 `d7670b5a-34e9-40f6-ac84-ec52996e52f3` 知识库中没有该节点类型的任何知识
