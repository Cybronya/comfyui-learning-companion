---
name: text_to_image_lora_sampler_clip_316
type: Text To Image
frequency: 6
level: strong
coverage: 0.889833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2110465965740879873.json, 图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json, 图片生成/图生图/参考图一键调色图生图，色调风格秒级对齐大师级色彩_2112625189052837889.json, 图片生成/图生图/参考图一键调色工作流｜色调氛围轻松对齐超省心_2112490868165931010.json, 图片生成/文生图/图生图任意角度转换双图版｜Qwen Image2.1 多角度出图更立体_2105540395974348802.json, 视频生成/文生视频/AI角色姿态导演台Character Pose Director，文生视频图生视频姿势精准控制_2103202510185000962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_316

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/千问IMAGE2.1换头工作流，图生图角色一致性完美保留_2110465965740879873.json、图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json、图片生成/图生图/参考图一键调色图生图，色调风格秒级对齐大师级色彩_2112625189052837889.json、图片生成/图生图/参考图一键调色工作流｜色调氛围轻松对齐超省心_2112490868165931010.json、图片生成/文生图/图生图任意角度转换双图版｜Qwen Image2.1 多角度出图更立体_2105540395974348802.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 4/6 个有
- `QwenImage21Cache` —— 4/6 个有
- `ImageScale` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `Get resolution [Crystools]` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `TextGenerate` —— 1/6 个有
- `VNCCS_PoseStudio` —— 1/6 个有

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
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
