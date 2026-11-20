---
name: unknown_workflow_sampler_clip_unet_354
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.883333
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPTextEncode, CustomAddLabel, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, Int, JjkText, KSamplerSelect, LayerUtility: PurgeVRAM V2, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SRPO-image-generation-电影级皮肤质感-洗图_2025737603282112514.json, 图片生成/文生图/SRPO-image-generation-电影级皮肤质感-文生图-自动提示词_2025756081611345922.json, 图片生成/文生图/SRPO-image-generation-电影级皮肤质感-文生图_1973761942366064641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_354

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SRPO-image-generation-电影级皮肤质感-洗图_2025737603282112514.json、图片生成/文生图/SRPO-image-generation-电影级皮肤质感-文生图-自动提示词_2025756081611345922.json、图片生成/文生图/SRPO-image-generation-电影级皮肤质感-文生图_1973761942366064641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CustomAddLabel`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `SeedVR2` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `BatchTextReplace` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
