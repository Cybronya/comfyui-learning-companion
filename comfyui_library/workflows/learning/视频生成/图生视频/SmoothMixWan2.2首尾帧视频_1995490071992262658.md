---
key: 视频生成/图生视频/SmoothMixWan2.2首尾帧视频_1995490071992262658.json
name: SmoothMixWan2.2首尾帧视频_1995490071992262658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SmoothMixWan2.2首尾帧视频_1995490071992262658.json
hash: cc6c0aa1c9a5e985
coverage: 0.833333
learned_at: 2026-10-15 22:33:23
nodes: [Int, PrimitiveStringMultiline, Joy_caption_two_load, Joy_caption_two, PreviewAny, Joy_caption_two, PreviewAny, PrimitiveStringMultiline, RH_LLMAPI_NODE, Joy_caption_two_load, LayerUtility: BooleanOperatorV2, LayerUtility: If , Int, Int, PreviewAny, String, ImpactSwitch, ImageResizeKJv2, UNETLoader, UNETLoader, CLIPVisionEncode, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, CLIPLoader, ImageResizeKJv2, CLIPVisionLoader, VAELoader, CLIPVisionEncode, WanFirstLastFrameToVideo, WanMoeKSampler, VAEDecode, INTConstant, SimpleMath+, easy cleanGpuUsed, CLIPTextEncode, PreviewAny, LayerUtility: TextJoin, VHS_VideoCombine, Int, DF_Integer, PrimitiveStringMultiline, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/SmoothMixWan2.2首尾帧视频_1995490071992262658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995490071992262658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（48 个）：
- `Int`
- `PrimitiveStringMultiline`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `PreviewAny`
- `Joy_caption_two`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `Joy_caption_two_load`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `Int`
- `Int`
- `PreviewAny`
- `String`
- `ImpactSwitch`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LayerUtility: TextJoin`
- `VHS_VideoCombine`
- `Int`
- `DF_Integer`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **83%**（40/48）

**有卡**：`Int`、`Joy_caption_two_load`、`Joy_caption_two`、`RH_LLMAPI_NODE`、`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`String`、`ImageResizeKJv2`、`UNETLoader`、`CLIPVisionEncode`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`WanFirstLastFrameToVideo`、`WanMoeKSampler`、`VAEDecode`、`INTConstant`、`SimpleMath+`、`easy cleanGpuUsed`、`LayerUtility: TextJoin`、`VHS_VideoCombine`、`DF_Integer`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode
