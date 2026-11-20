---
name: unknown_workflow_sampler_clip_unet_143
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8676
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/😶_🌫️FLUX新王炸 Klein 文生图急速10秒出图😶_🌫️_2012094524113297409.json, 图片生成/文生图/😼FLUX2-KLEIN 文生图、单图、多图编辑合集@言灵ru_2014708517436919810.json, 平台全量/FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977.json, 平台全量/FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082.json, 平台全量/Flux2 Klein增加皮肤细节+高清放大+增强细节  图像修复高清放大 高清修复+去AI感_2016708999902662657.json, 平台全量/Flux2-Klein-9B 单图编辑_2021972439718170625.json, 平台全量/Flux2-Klein9b优化皮肤质感 添加真实感细节  高清放大 增加细节 去除AI塑料感 优化皮_2031199411719643137.json, 平台全量/Flux2-klein单图+双图编辑工作流_2046154927646449666.json, 平台全量/Klein 9b 黑兽BFS 最强换头工作流_2044806861702041602.json, 平台全量/Klein 9b 黑兽BFS 最强换头工作流（双图对比同出）_2045053032420876290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_143

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/😶_🌫️FLUX新王炸 Klein 文生图急速10秒出图😶_🌫️_2012094524113297409.json、图片生成/文生图/😼FLUX2-KLEIN 文生图、单图、多图编辑合集@言灵ru_2014708517436919810.json、平台全量/FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977.json、平台全量/FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082.json、平台全量/Flux2 Klein增加皮肤细节+高清放大+增强细节  图像修复高清放大 高清修复+去AI感_2016708999902662657.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `ReferenceLatent` —— 9/10 个有
- `VAEEncode` —— 9/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `GetImageSize` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 4/10 个有
- `Seed (rgthree)` —— 4/10 个有
- `ImpactSwitch` —— 3/10 个有
- `PlaySound|pysssss` —— 3/10 个有
- `easy int` —— 2/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `PreviewImageLam` —— 1/10 个有
- `easy getNode` —— 1/10 个有
- `easy setNode` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
