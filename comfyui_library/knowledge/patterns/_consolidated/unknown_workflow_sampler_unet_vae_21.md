---
name: unknown_workflow_sampler_unet_vae_21
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.860526
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3-图生视频_2088576094667632642.json, 视频生成/图生视频/MinimaxI2V_2084500141607841794.json, 视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2092340433505574914.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2096278611857862657.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2092310874190073858.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2092935184156024834.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2105856274675093506.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2109460890293727233.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2109652415707443202.json, 视频生成/图生视频/minimaxH3开源版首帧生视频(8step加速)_2092324995224662017.json, 视频生成/图生视频/minimax图出视频_2084274641455112193.json, 视频生成/图生视频/minnimax h3 首尾帧生视频（4步加速）_2085544529314271234.json, 视频生成/图生视频/minnimax h3 首帧生视频（8步加速）_2085549343964221442.json, 视频生成/图生视频/漫剧林辰_2103760332870217729.json, 视频生成/图生视频/短剧漫剧参考图生视频_2103117172716429314.json, 视频生成/图生视频/自我介绍_2110222353635561474.json, 视频生成/图生视频/走秀_2110212966074376193.json, 视频生成/文生视频/MiniMax-H3文生视频人物类特效数字人工作流_2090000867746476033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_21

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3-图生视频_2088576094667632642.json、视频生成/图生视频/MinimaxI2V_2084500141607841794.json、视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json、视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2092340433505574914.json、视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2096278611857862657.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 18/19 个有
- `ResolutionSelector` —— 18/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/19 个有
- `LoraLoaderModelOnly` —— 15/19 个有
- `MiniMaxH3ImageToVideo` —— 15/19 个有
- `PathchSageAttentionKJ` —— 9/19 个有
- `CR Text` —— 5/19 个有
- `MiniMaxH3ReferenceToVideo` —— 4/19 个有
- `PreviewImage` —— 4/19 个有
- `JjkText` —— 3/19 个有
- `PrimitiveStringMultiline` —— 3/19 个有
- `EasyCache` —— 2/19 个有
- `Int` —— 2/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/19 个有
- `ResizeImageMaskNode` —— 2/19 个有
- `DF_Int_to_Float` —— 1/19 个有
- `LoraLoader` —— 1/19 个有
- `LoraLoaderBypassModelOnly` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
