---
name: unknown_workflow_lora_sampler_clip_153
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.853
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima-702-护士长_2072661208766959618.json, 平台全量/Flux2 Klein9b 提取服装精修 服装提取 3D虚拟模特 服装展示 隐形模特 移除褶皱_2020698339708243970.json, 平台全量/Flux2-Klein9b 万能提取服装 服装3D立体展示效果 精修褶皱 修复移除褶皱_2025379732933578754.json, 平台全量/Flux2-Klein9b 万能提取服装 服装3D立体展示效果 精修褶皱 修复移除褶皱_2025804639882448898.json, 平台全量/Flux2_Klein光影写实风格颜色匹配_2062402292011323393.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima-702-护士长_2072661208766959618.json、平台全量/Flux2 Klein9b 提取服装精修 服装提取 3D虚拟模特 服装展示 隐形模特 移除褶皱_2020698339708243970.json、平台全量/Flux2-Klein9b 万能提取服装 服装3D立体展示效果 精修褶皱 修复移除褶皱_2025379732933578754.json、平台全量/Flux2-Klein9b 万能提取服装 服装3D立体展示效果 精修褶皱 修复移除褶皱_2025804639882448898.json、平台全量/Flux2_Klein光影写实风格颜色匹配_2062402292011323393.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ColorMatch` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `FLS_SamplerV4` —— 1/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Latent Noise Injection` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `Power Lora Loader (rgthree)` —— 1/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `SplitSigmasDenoise` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
