---
name: unknown_workflow_inpaint_sampler_clip_32
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.909571
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/物体擦除 _ OneReward-Fill_1966334211617665026.json, 图片生成/图生图/🦖flux_fill_inpaint局部重绘画_1894586983191326722.json, 平台全量/FLUX Fill Inpaint_2070991751468376066.json, 平台全量/Fill-OneReward-物体移除_1968880946558717954.json, 平台全量/Flux-fill-消除万物，消除水印_2020027527921668097.json, 平台全量/Flux局部重绘丨最强 局部重绘无痕一键生成_1959068412154687489.json, 平台全量/【Onereward】完美无缝扩图工作流_2008003276955983874.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/物体擦除 _ OneReward-Fill_1966334211617665026.json、图片生成/图生图/🦖flux_fill_inpaint局部重绘画_1894586983191326722.json、平台全量/FLUX Fill Inpaint_2070991751468376066.json、平台全量/Fill-OneReward-物体移除_1968880946558717954.json、平台全量/Flux-fill-消除万物，消除水印_2020027527921668097.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `RH_Translator` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `ImageAndMaskPreview` —— 2/7 个有
- `LayerUtility: ImageReel` —— 2/7 个有
- `LayerUtility: ImageReelComposit` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `CLIPTextEncode (NSP)` —— 1/7 个有
- `DapaoImageAspectRatioResizeNode` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
