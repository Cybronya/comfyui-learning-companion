---
name: text_to_image_lora_sampler_clip_170
type: Text To Image
frequency: 10
level: weak
coverage: 0.878
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问2.1文生图_2103829231951241218.json, 图片生成/文生图/千问2.1文生图官方原生架构｜一键出图带海报制作｜新手友好_2104813513557504002.json, 图片生成/文生图/千问2.1文生图自动优化版｜一句话提示词直出精美图片_2103726338984210433.json, 图片生成/文生图/千问2.1文生图｜轻量好上手 文生图出图稳定效果在线_2104035483096539138.json, 图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json, 图片生成/文生图/千问iamge2.1文生图工作流｜官方同款画质一键直出_2103062439452569601.json, 数字人/数字人/Qwen 2.1透明背景抠图，一键生成PNG透明图生图工具_2102899365059846146.json, 数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json, 视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json, 视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_170

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/千问2.1文生图_2103829231951241218.json、图片生成/文生图/千问2.1文生图官方原生架构｜一键出图带海报制作｜新手友好_2104813513557504002.json、图片生成/文生图/千问2.1文生图自动优化版｜一句话提示词直出精美图片_2103726338984210433.json、图片生成/文生图/千问2.1文生图｜轻量好上手 文生图出图稳定效果在线_2104035483096539138.json、图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 8/10 个有
- `PreviewImage` —— 7/10 个有
- `孤海注释` —— 7/10 个有
- `FastGroupsBypassSwitch` —— 6/10 个有
- `ResolutionSelector` —— 6/10 个有
- `TextGenerateLTX2Prompt` —— 5/10 个有
- `LoadImage` —— 3/10 个有
- `QwenImage21Cache` —— 3/10 个有
- `TextCombinerTwo` —— 3/10 个有
- `CM_FloatToInt` —— 2/10 个有
- `EmptyImage` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `SaveImageAdvanced` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 10 | 0% |
| 高度 | 80 | 80 - 1024 | 10 | 0% |
| 采样步数 | 4 | 4 - 50 | 10 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 10 | 75% |
| 采样算法 | er_sde | - | 10 | 90% |
| 调度器 | beta | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 50，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 90%
- 调度器 最常用 beta，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
