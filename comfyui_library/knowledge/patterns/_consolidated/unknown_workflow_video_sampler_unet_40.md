---
name: unknown_workflow_video_sampler_unet_40
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9738
common_nodes: [BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, HunyuanImageToVideo, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, TextEncodeHunyuanVideo_ImageToVideo, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/全网首发，官方混元I2V正确版工作流_1897656263986073602.json, 视频生成/图生视频/图生视频  Comfyorg 局部动作_2030823409466220546.json, 视频生成/图生视频/图生视频  Comfyorg 局部动作_2046840508722454530.json, 视频生成/图生视频/图生视频 快速生成_2031906239327772674.json, 视频生成/图生视频/最新腾讯混元图生视频，速度比万相快不少_1897851566873858049.json, 视频生成/图生视频/混元官方I2V图生视频_1897633108676530177.json, 视频生成/图生视频/混元视频 I2V 图生视频 Comfyorg 官方工作流_1897641777338208257.json, 视频生成/图生视频/混元视频+I2V+图生视频+Comfyully工作流_2041316621637128193.json, 视频生成/图生视频/混元视频+I2V+图生视频_2052192560470339585.json, 视频生成/图生视频/腾讯官方混元图生视频(ComfyUI)_1897700159466491905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/全网首发，官方混元I2V正确版工作流_1897656263986073602.json、视频生成/图生视频/图生视频  Comfyorg 局部动作_2030823409466220546.json、视频生成/图生视频/图生视频  Comfyorg 局部动作_2046840508722454530.json、视频生成/图生视频/图生视频 快速生成_2031906239327772674.json、视频生成/图生视频/最新腾讯混元图生视频，速度比万相快不少_1897851566873858049.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
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
- `Int` —— 5/10 个有
- `TextInput_` —— 5/10 个有
- `ImageFromBatch` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `Note Plus (mtb)` —— 2/10 个有
- `Primitive integer [Crystools]` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `ColorMatch` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `PatchModelPatcherOrder` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `Primitive string [Crystools]` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
