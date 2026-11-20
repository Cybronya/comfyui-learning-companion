---
name: text_to_image_lora_sampler_clip_25
type: Text To Image
frequency: 22
level: strong
coverage: 0.876273
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3_MAX智能运镜AI看图自动运镜图生图处理工作流_2101761496228388866.json, 图片生成/图生图/Image2.5高精度图生图处理生成工具_2100287923240398849.json, 图片生成/图生图/MOSS Text to Image 2K Turbo 文生图图生图极速工具_2114119482594648066.json, 图片生成/图生图/Moss-image 8步加速文生图，图生图辅助提速不等待_2112701805070213121.json, 图片生成/图生图/Moss-image 文生图8步加速版｜图生图洗图更高效_2112404734073204738.json, 图片生成/图生图/Moss-image 文生图提示词增强｜一句话出好图_2112406284036296705.json, 图片生成/图生图/Moss-image提示词增强文生图，图生图辅助出图更省心_2112620573389049858.json, 图片生成/文生图/Flux 3_Image_Klein开源版文生图｜角色设计写真一把好手_2111303591293177858.json, 图片生成/文生图/Flux3 Klein提示词增强文生图 创意直出高效处理工具_2113710948639924225.json, 图片生成/文生图/Flux3 Klein文生图提示词增强 创意直出省心生成工具_2113709466570022914.json, 图片生成/文生图/Flux3-klein提示词增强文生图｜创意画面直出更轻松省事_2113539868348469249.json, 图片生成/文生图/Flux3-klein文生图带提示词增强｜一键自动扩写出好图_2111269274059890689.json, 图片生成/文生图/Flux3-klein文生图提示词增强版｜创意出图省心利器_2114028428172292098.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2111610313010401282.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113183047603539969.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113198789153615874.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113543215390482434.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113546638164848641.json, 图片生成/文生图/Flux3-klein文生图提示词增强｜创意直出更省心_2114072279226347522.json, 图片生成/文生图/Flux3-klein文生图提示词自动增强｜创意直出省心出图_2113538281471303681.json, 图片生成/文生图/MOSS SFT 文生图Comfyui官方流｜海报制作利器_2112476243789697025.json, 视频生成/文生视频/MOSS SFT ComfyUI官方版工作流，文生视频基础管线稳定可靠_2114560619595788289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/H3_MAX智能运镜AI看图自动运镜图生图处理工作流_2101761496228388866.json、图片生成/图生图/Image2.5高精度图生图处理生成工具_2100287923240398849.json、图片生成/图生图/MOSS Text to Image 2K Turbo 文生图图生图极速工具_2114119482594648066.json、图片生成/图生图/Moss-image 8步加速文生图，图生图辅助提速不等待_2112701805070213121.json、图片生成/图生图/Moss-image 文生图8步加速版｜图生图洗图更高效_2112404734073204738.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 20/22 个有
- `PrimitiveStringMultiline` —— 20/22 个有
- `ResolutionSelector` —— 20/22 个有
- `TextGenerate` —— 18/22 个有
- `孤海注释` —— 18/22 个有
- `CR Prompt Text` —— 16/22 个有
- `ConditioningZeroOut` —— 12/22 个有
- `easy showAnything` —— 12/22 个有
- `EmptyImage` —— 3/22 个有
- `LoadImage` —— 2/22 个有
- `SkipLayerGuidanceDiTSimple` —— 2/22 个有
- `PreviewAny` —— 1/22 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/22 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 1/22 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/22 个有
- `SaveVideo` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（29/22 个样本）：Steps较低可能导致细节不足
