---
name: unknown_workflow_lora_clip_unet_5
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.363222
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, GetNode, LoraLoaderModelOnly, PrimitiveInt, ResolutionSelector, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MOSS 双采高清+SeedVR2工作流_2115697232925253633.json, 图片生成/文生图/MOSS单采_双采合集工作流_2112898314982215681.json, 图片生成/文生图/MOSS双采工作流_2114740900021760001.json, 图片生成/文生图/MOSS双采工作流_2115434715992911874.json, 图片生成/文生图/MOSS双采工作流_2115660188559695874.json, 图片生成/文生图/moss文生图V2版_2115880638334201857.json, 图片生成/文生图/moss文生图V2版_2115990806854197249.json, 平台全量/MOSS双采工作流_2118188578537820161.json, 平台全量/MOSS双采真实世界-1109_2119488785691004930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/MOSS 双采高清+SeedVR2工作流_2115697232925253633.json、图片生成/文生图/MOSS单采_双采合集工作流_2112898314982215681.json、图片生成/文生图/MOSS双采工作流_2114740900021760001.json、图片生成/文生图/MOSS双采工作流_2115434715992911874.json、图片生成/文生图/MOSS双采工作流_2115660188559695874.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：36%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `GetNode`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 8/9 个有
- `SeedVR2LoadDiTModel` —— 8/9 个有
- `SeedVR2LoadVAEModel` —— 8/9 个有
- `SeedVR2VideoUpscaler` —— 8/9 个有
- `SkipLayerGuidanceDiTSimple` —— 8/9 个有
- `KSamplerAdvanced` —— 7/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `PrimitiveFloat` —— 7/9 个有
- `Fast Groups Muter (rgthree)` —— 6/9 个有
- `INTConstant` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `Label (rgthree)` —— 5/9 个有
- `KSampler` —— 3/9 个有
- `LazyCache` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `TextGenerate` —— 2/9 个有
- `LoadImage` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 78% |
| Prompt 约束强度(CFG) | 50 | 2.5 - 50 | 9 | 50% |
| 采样算法 | 3 | 3 - 3 | 7 | 100% |
| 调度器 | er_sde | - | 9 | 67% |
| 重绘幅度 | simple | - | 9 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 50，观测区间 2.5 - 50，9 个样本，取值分散，一致性仅 50%
- 采样算法 中位数 3，观测区间 3 - 3，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，9 个样本，一致性 67%
- 重绘幅度 最常用 simple，9 个样本，一致性 78%
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
