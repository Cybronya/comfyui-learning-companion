---
name: text_to_image_lora_sampler_clip_195
type: Text To Image
frequency: 6
level: strong
coverage: 0.906333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Topaz星光高清放大模型｜数毛党最爱地表最强，视频超分拉满_2107366759350235137.json, 图片生成/文生图/G-image-2.5文生图极速API版｜秒级出图效率拉满_2098732116275195905.json, 图片生成/文生图/G-image-2.5文生图高品质API版｜出图质感在线_2098726914138664961.json, 图片生成/文生图/G-image-2.5文生图高品质版 文本到图像精细生成_2098294330913021954.json, 图片生成/文生图/全能图片G2.5经济版Sunburst文生图处理生成工具_2101383650859376641.json, 图片生成/文生图/视频超分工作流_2101989284810153986.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_195

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Topaz星光高清放大模型｜数毛党最爱地表最强，视频超分拉满_2107366759350235137.json、图片生成/文生图/G-image-2.5文生图极速API版｜秒级出图效率拉满_2098732116275195905.json、图片生成/文生图/G-image-2.5文生图高品质API版｜出图质感在线_2098726914138664961.json、图片生成/文生图/G-image-2.5文生图高品质版 文本到图像精细生成_2098294330913021954.json、图片生成/文生图/全能图片G2.5经济版Sunburst文生图处理生成工具_2101383650859376641.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/6 个有
- `SaveImage` —— 4/6 个有
- `LoadVideo` —— 2/6 个有
- `RH_Astra` —— 2/6 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `JWInteger` —— 1/6 个有
- `QZ_ResolutionPreset` —— 1/6 个有
- `RH_RhartImageG25OfficialTokenFlareTextToImage` —— 1/6 个有
- `RH_RhartImageG25SunburstTextToImage` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
