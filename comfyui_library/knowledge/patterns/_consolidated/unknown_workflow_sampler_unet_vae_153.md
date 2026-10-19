---
name: unknown_workflow_sampler_unet_vae_153
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.61775
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa V1-SLA加速-MiniMax H3_2091698361979203585.json, 视频生成/图生视频/MiniMax H3 Ref2VA开源版-ComfyUI官方-量化加速-视频编辑-人物替换_2084895356386635778.json, 视频生成/图生视频/数字人对口型-MiniMax H3 Ref2VA开源版-ComfyUI官方-量化加速_2084948483420803073.json, 视频生成/图生视频/数字人对口型工作流_2087435972651868162.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Dasiwa V1-SLA加速-MiniMax H3_2091698361979203585.json、视频生成/图生视频/MiniMax H3 Ref2VA开源版-ComfyUI官方-量化加速-视频编辑-人物替换_2084895356386635778.json、视频生成/图生视频/数字人对口型-MiniMax H3 Ref2VA开源版-ComfyUI官方-量化加速_2084948483420803073.json、视频生成/图生视频/数字人对口型工作流_2087435972651868162.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `Audio Cut (mtb)` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `VAEDecodeAudio` —— 2/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `SolAttnMiniMax` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
