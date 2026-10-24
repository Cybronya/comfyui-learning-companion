---
name: text_to_image_lora_sampler_clip_154
type: Text To Image
frequency: 10
level: strong
coverage: 0.8579
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3_MAX智能运镜AI看图自动运镜图生图处理工作流_2101761496228388866.json, 图片生成/图生图/Image2.5高精度图生图处理生成工具_2100287923240398849.json, 图片生成/图生图/Qwen Image 2.1 IN 极速版全能编辑，2K超清透明通道十图极限融合_2103213714240528385.json, 图片生成/图生图/千问IMAGE2.1换头工作流 人物面部精准替换_2108707879661428738.json, 视频生成/图生视频/H3 MAX旗舰模型图生视频 工作流让静态图片动起来_2098636207260524546.json, 视频生成/图生视频/H3 MAX旗舰模型图生视频｜让静态图片自然动起来_2098699818653802497.json, 视频生成/图生视频/H3 MAX首尾帧工作流｜旗舰模型双图过渡生成_2095597681195446273.json, 视频生成/图生视频/H3 Max智能运镜工作流 AI看图自动运镜处理_2100658647239053314.json, 视频生成/图生视频/H3 Max智能运镜工作流 AI看图自动运镜处理_2100669399102476290.json, 视频生成/文生视频/AI看图自动运镜｜H3 MAX智能运镜文生视频_2095836375957458946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/H3_MAX智能运镜AI看图自动运镜图生图处理工作流_2101761496228388866.json、图片生成/图生图/Image2.5高精度图生图处理生成工具_2100287923240398849.json、图片生成/图生图/Qwen Image 2.1 IN 极速版全能编辑，2K超清透明通道十图极限融合_2103213714240528385.json、图片生成/图生图/千问IMAGE2.1换头工作流 人物面部精准替换_2108707879661428738.json、视频生成/图生视频/H3 MAX旗舰模型图生视频 工作流让静态图片动起来_2098636207260524546.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `EmptyImage` —— 2/10 个有
- `TextEncodeQwenImage21` —— 2/10 个有
- `Get resolution [Crystools]` —— 1/10 个有
- `ImageCompositeMasked` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/10 个有
- `ResolutionSelector` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
