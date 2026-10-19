---
name: text_to_image_video_lora_sampler_63
type: Text To Image
frequency: 11
level: strong
coverage: 0.838818
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, JjkText, KSampler, LoraLoaderModelOnly, Seed, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus Bernini, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerExtraArgs, WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Bernini视频去水印天花板｜无痕去字幕logo画质如初_2107670519372935170.json, 视频生成/图生视频/Bernini高清视频编辑去水印天花板｜无痕去字幕去logo，画质如初_2107328479384653825.json, 视频生成/图生视频/Bernini高清视频编辑去水印天花板｜无痕去字幕去logo，画质如初_2107441049831559170.json, 视频生成/图生视频/bernini局部衣服修改｜电商带货视频编辑图生视频处理_2094718463712518146.json, 视频生成/图生视频/带货主播手中产品替换｜电商视频生视频一键搞定_2095545842093617153.json, 视频生成/图生视频/电商带货bernini局部衣服修改｜视频生视频换装更自由_2106265187983646722.json, 视频生成/图生视频/电商带货产品替换｜视频图生视频主播手持商品更换_2091243839599239169.json, 视频生成/图生视频/电商带货替换主播手中产品工作流，视频生视频图生视频处理工具_2106844793283371009.json, 视频生成/图生视频/电商带货替换主播手中产品工作流，视频生视频图生视频处理工具_2110530638565699586.json, 视频生成/图生视频/电商带货替换主播手中产品视频生视频图生视频_2087331268609527809.json, 视频生成/图生视频/电商带货视频换产品神器｜主播手中商品随意替换，不用重新拍片_2099515530515402753.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Bernini视频去水印天花板｜无痕去字幕logo画质如初_2107670519372935170.json、视频生成/图生视频/Bernini高清视频编辑去水印天花板｜无痕去字幕去logo，画质如初_2107328479384653825.json、视频生成/图生视频/Bernini高清视频编辑去水印天花板｜无痕去字幕去logo，画质如初_2107441049831559170.json、视频生成/图生视频/bernini局部衣服修改｜电商带货视频编辑图生视频处理_2094718463712518146.json、视频生成/图生视频/带货主播手中产品替换｜电商视频生视频一键搞定_2095545842093617153.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `INTConstant`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `Seed`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus Bernini`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SamplerExtraArgs`
- `WanAnimatePlus Samplerv2`
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `VHS_VideoInfoLoaded` —— 8/11 个有
- `easy showAnything` —— 8/11 个有
- `孤海注释` —— 8/11 个有
- `EmptyImage` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `TextCombinerSix` —— 3/11 个有
- `VHS_VideoInfoSource` —— 3/11 个有
- `SaveImage` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
