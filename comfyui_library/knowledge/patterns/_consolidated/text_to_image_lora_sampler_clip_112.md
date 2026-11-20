---
name: text_to_image_lora_sampler_clip_112
type: Text To Image
frequency: 13
level: strong
coverage: 0.869692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能视频X-图生视频-官方稳定版｜创意图片处理一把梭_2114239665745256450.json, 图片生成/图生图/全能视频X图生视频官方稳定版 图像转视频处理生成工具_2113012166080163841.json, 图片生成/图生图/全能视频X图生视频官方稳定版 高质量动态生成_2109329783984320513.json, 图片生成/图生图/全能视频X图生视频官方稳定版，图片一键转动态视频效果稳定高清_2114416677403320322.json, 图片生成/图生图/全能视频X图生视频官方稳定版，图生图其它图片处理方案_2106812144393220097.json, 图片生成/图生图/全能视频X图生视频官方稳定版｜图生图其他创意图片处理_2090434947831132161.json, 图片生成/图生图/全能视频X官方稳定版｜图生视频一步出片创意无限_2108019355983376386.json, 图片生成/图生图/千府AI DLSS5洗图图生图处理生成工作流_2102177419565297665.json, 图片生成/图生图/千问2.1图像编辑多图参考｜精准修改指哪改哪｜其它图片处理全能_2104810356660064258.json, 图片生成/图生图/千问IMAGE2.1换头工作流 人物面部精准替换_2108707879661428738.json, 图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2110465965740879873.json, 图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2113459910682955778.json, 图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/全能视频X-图生视频-官方稳定版｜创意图片处理一把梭_2114239665745256450.json、图片生成/图生图/全能视频X图生视频官方稳定版 图像转视频处理生成工具_2113012166080163841.json、图片生成/图生图/全能视频X图生视频官方稳定版 高质量动态生成_2109329783984320513.json、图片生成/图生图/全能视频X图生视频官方稳定版，图片一键转动态视频效果稳定高清_2114416677403320322.json、图片生成/图生图/全能视频X图生视频官方稳定版，图生图其它图片处理方案_2106812144393220097.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 12/13 个有
- `SaveImage` —— 10/13 个有
- `RH_RhartVideoGOfficialImageToVideo` —— 7/13 个有
- `SaveVideo` —— 7/13 个有
- `TextEncodeQwenImage21` —— 5/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `Get resolution [Crystools]` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `StringConcatenate` —— 2/13 个有
- `TextGenerate` —— 2/13 个有
- `Anything Everywhere` —— 1/13 个有
- `EmptyImage` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `ImageCASharpening+` —— 1/13 个有
- `RH_DLSS5Enhance` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足
