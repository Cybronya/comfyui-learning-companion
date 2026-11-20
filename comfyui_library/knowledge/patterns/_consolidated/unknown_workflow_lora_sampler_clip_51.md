---
name: unknown_workflow_lora_sampler_clip_51
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.915889
common_nodes: [CLIPLoader, CLIPTextEncode, CR Seed, DiffusionModelLoaderKJ, DuckHideNode, INTConstant, ImageResizeKJv2, ImpactWildcardProcessor, KSamplerAdvanced, LoadImage, MathExpression|pysssss, ModelSamplingSD3, Power Lora Loader (rgthree), PrimitiveFloat, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/122156745_2047913329334685698.json, 视频生成/图生视频/122698483_2045055007434739714.json, 视频生成/图生视频/122758028_2042151948933140482.json, 视频生成/图生视频/232cd9d3_2049022280566575105.json, 视频生成/图生视频/7e11aed2_2034110995689377794.json, 视频生成/图生视频/9989ddf8_2044656720277934081.json, 视频生成/图生视频/ab45f051_2045682255523221506.json, 视频生成/图生视频/b636ee4c_2045866449708785665.json, 视频生成/图生视频/d6c41743_2046213920049860609.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/122156745_2047913329334685698.json、视频生成/图生视频/122698483_2045055007434739714.json、视频生成/图生视频/122758028_2042151948933140482.json、视频生成/图生视频/232cd9d3_2049022280566575105.json、视频生成/图生视频/7e11aed2_2034110995689377794.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `DiffusionModelLoaderKJ`
- `DuckHideNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImpactWildcardProcessor`
- `KSamplerAdvanced`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `Power Lora Loader (rgthree)`
- `PrimitiveFloat`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 8/9 个有
- `LayerUtility: PurgeVRAM` —— 8/9 个有
- `ModelPatchTorchSettings` —— 8/9 个有
- `PainterI2V` —— 8/9 个有
- `PathchSageAttentionKJ` —— 8/9 个有
- `PrimitiveInt` —— 8/9 个有
- `WanVideoNAG` —— 8/9 个有
- `CLIPVisionLoader` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `WanImageToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 100% |
| Prompt 约束强度(CFG) | 20 | 10 - 20 | 9 | 83% |
| 采样算法 | 1 | 1 - 1.1 | 9 | 97% |
| 调度器 | euler_ancestral | - | 9 | 100% |
| 重绘幅度 | normal | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 10 - 20，9 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1.1，9 个样本，取值集中（一致性 97%）
- 调度器 最常用 euler_ancestral，9 个样本，一致性 100%
- 重绘幅度 最常用 normal，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
