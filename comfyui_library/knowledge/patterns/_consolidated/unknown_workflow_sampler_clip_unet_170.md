---
name: unknown_workflow_sampler_clip_unet_170
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.912889
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux2 Klein白底图批量刷图-9B版官方版（单图编辑）_2026559810073792514.json, 平台全量/Flux2-Klein-单图编辑_2071879799651528705.json, 平台全量/Flux2-Klein_9B建筑设计迁移_2032648193267212289.json, 平台全量/Flux2-klein单图+双图编辑工作流_2067302840548290562.json, 平台全量/Flux2-klein双图操作流_2013135947860287489.json, 平台全量/Flux2写实摄影 klein单图+双图编辑 真实拍摄_2013081939758026754.json, 平台全量/Klein 人物替换｜双图对照版_2098720785874644994.json, 平台全量/图片-批量处理_2022498155601858562.json, 数字人/数字人/Flux2 Klein 多图编辑 加速版_2012172771391971330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_170

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Flux2 Klein白底图批量刷图-9B版官方版（单图编辑）_2026559810073792514.json、平台全量/Flux2-Klein-单图编辑_2071879799651528705.json、平台全量/Flux2-Klein_9B建筑设计迁移_2032648193267212289.json、平台全量/Flux2-klein单图+双图编辑工作流_2067302840548290562.json、平台全量/Flux2-klein双图操作流_2013135947860287489.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `EmptyFlux2LatentImage` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `SaveImage` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `GetNode` —— 3/9 个有
- `Int` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `HAIGC_SaveImagesToZip` —— 2/9 个有
- `JjkText` —— 2/9 个有
- `CR Latent Batch Size` —— 1/9 个有
- `FluxKontextImageScale` —— 1/9 个有
- `ImageBatchToList` —— 1/9 个有
- `LayerUtility: SaveImagePlusV2` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `SGUNLoadImageBatch` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
