---
name: unknown_workflow_sampler_unet_vae_171
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.856
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_LipSync_2116362537133498370.json, 视频生成/图生视频/MiniMax_H3_LipSync_2116379525620789249.json, 视频生成/图生视频/MiniMax_H3_R2V_3参考图_LightX2V_4步_2090336616714956801.json, 视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json, 视频生成/图生视频/MiniMax_H3音画同步参考工作流_2116344470043185154.json, 视频生成/图生视频/Minimax H3 图生视频工作流｜AI海报动画生成｜最强免费开源视频模型_2089969033876692993.json, 视频生成/图生视频/Minimax H3 多参视频生成_2089987673200091137.json, 视频生成/图生视频/MinimaxH3音频驱动视频生成_2091411487955972097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_171

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_LipSync_2116362537133498370.json、视频生成/图生视频/MiniMax_H3_LipSync_2116379525620789249.json、视频生成/图生视频/MiniMax_H3_R2V_3参考图_LightX2V_4步_2090336616714956801.json、视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json、视频生成/图生视频/MiniMax_H3音画同步参考工作流_2116344470043185154.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 7/8 个有
- `PathchSageAttentionKJ` —— 7/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `VAEDecodeAudio` —— 5/8 个有
- `EasyCache` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `ModelPatchTorchSettings` —— 3/8 个有
- `SoundFlow_GetLength` —— 3/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `SaveImageAdvanced` —— 1/8 个有
- `SpectrumSDXLBatch` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
