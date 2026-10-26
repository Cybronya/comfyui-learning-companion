---
name: unknown_workflow_sampler_clip_vae_46
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9028
common_nodes: [AdvancedVisionLoader, ApplyFBCacheOnModel, CLIPTextEncode, CLIPVisionEncode, DF_Get_image_size, EmptySD3LatentImage, FluxGuidance, JWImageResizeByLongerSide, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingFlux, Note Plus (mtb), SaveImage, StyleModelApply, StyleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705.json, 图片生成/图生图/Flux Krea Redux对比（384版）_1950998578217025537.json, "图片生成/图生图/新版三件套Flex,Redux,Clipvision512双图融合加速可调权重工作流_1912505294071525378.json", "图片生成/图生图/混用老版Flux,新版Redux,Clipvision512双图融合加速可调权重工作流_1912505330801045505.json", 图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_46

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705.json、图片生成/图生图/Flux Krea Redux对比（384版）_1950998578217025537.json、图片生成/图生图/新版三件套Flex,Redux,Clipvision512双图融合加速可调权重工作流_1912505294071525378.json、图片生成/图生图/混用老版Flux,新版Redux,Clipvision512双图融合加速可调权重工作流_1912505330801045505.json、图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `AdvancedVisionLoader`
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DF_Get_image_size`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingFlux`
- `Note Plus (mtb)`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 4/5 个有
- `BasicGuider` —— 4/5 个有
- `BasicScheduler` —— 4/5 个有
- `CheckpointLoaderSimple` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `RandomNoise` —— 4/5 个有
- `SamplerCustomAdvanced` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `ImpactSwitch` —— 3/5 个有
- `StyleModelAdvancedApply` —— 3/5 个有
- `UNETLoader` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Flex2Conditioner` —— 1/5 个有
- `KSampler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | deis | - | 1 | 100% |
| 调度器 | beta | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
