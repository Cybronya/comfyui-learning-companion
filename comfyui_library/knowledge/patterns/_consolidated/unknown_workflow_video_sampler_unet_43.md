---
name: unknown_workflow_video_sampler_unet_43
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.96725
common_nodes: [BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, HunyuanImageToVideo, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, TextEncodeHunyuanVideo_ImageToVideo, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1897656263986073602.json, 视频生成/图生视频/2030823409466220546.json, 视频生成/图生视频/2046840508722454530.json, 视频生成/图生视频/2031906239327772674.json, 视频生成/图生视频/1897633108676530177.json, 视频生成/图生视频/混元视频 I2V 图生视频 Comfyorg 官方工作流_1897641777338208257.json, 视频生成/图生视频/2041316621637128193.json, 视频生成/图生视频/2052192560470339585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1897656263986073602.json、视频生成/图生视频/2030823409466220546.json、视频生成/图生视频/2046840508722454530.json、视频生成/图生视频/2031906239327772674.json、视频生成/图生视频/1897633108676530177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `HunyuanImageToVideo`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/8 个有
- `TextInput_` —— 5/8 个有
- `JjkText` —— 2/8 个有
- `ColorMatch` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PatchModelPatcherOrder` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
