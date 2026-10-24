---
name: unknown_workflow_sampler_clip_vae_34
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.921833
common_nodes: [AdvancedVisionLoader, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json, 图片生成/图生图/Flux Krea Redux对比（384版）_1950998578217025537.json, 图片生成/图生图/Redux 512 图生图_1915978476787007490.json, "图片生成/图生图/新版三件套Flex,Redux,Clipvision512双图融合加速可调权重工作流_1912505294071525378.json", "图片生成/图生图/混用老版Flux,新版Redux,Clipvision512双图融合加速可调权重工作流_1912505330801045505.json", 图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_34

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json、图片生成/图生图/Flux Krea Redux对比（384版）_1950998578217025537.json、图片生成/图生图/Redux 512 图生图_1915978476787007490.json、图片生成/图生图/新版三件套Flex,Redux,Clipvision512双图融合加速可调权重工作流_1912505294071525378.json、图片生成/图生图/混用老版Flux,新版Redux,Clipvision512双图融合加速可调权重工作流_1912505330801045505.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `AdvancedVisionLoader`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `JWImageResizeByLongerSide` —— 5/6 个有
- `ModelSamplingFlux` —— 5/6 个有
- `ApplyFBCacheOnModel` —— 4/6 个有
- `DF_Get_image_size` —— 4/6 个有
- `DualCLIPLoader` —— 4/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `Note Plus (mtb)` —— 4/6 个有
- `VAELoader` —— 4/6 个有
- `AddLabel` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `ImpactSwitch` —— 2/6 个有
- `StyleModelAdvancedApply` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `RH_Captioner` —— 1/6 个有
- `Text Concatenate (JPS)` —— 1/6 个有
- `VAEEncode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
