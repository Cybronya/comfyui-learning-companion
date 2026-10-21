---
name: text_to_image_lora_sampler_clip_76
type: Text To Image
frequency: 12
level: strong
coverage: 0.899083
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2102241527849373698.json, 图片生成/文生图/Qwen2.1 BF16官方文生图工作流｜海报制作字体设计一次到位_2102219743238385666.json, 图片生成/文生图/Qwen2.1_BF16官方文生图工作流｜海报制作字体设计一次到位_2104058681204764674.json, 图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json, 图片生成/文生图/qwen image2.1文生图利器｜数字人海报制作一步搞定_2104529003418836993.json, 图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json, 图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102267329873801217.json, 图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102320781945561089.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2105070911778021377.json, 图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json, 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Qwen image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2102241527849373698.json、图片生成/文生图/Qwen2.1 BF16官方文生图工作流｜海报制作字体设计一次到位_2102219743238385666.json、图片生成/文生图/Qwen2.1_BF16官方文生图工作流｜海报制作字体设计一次到位_2104058681204764674.json、图片生成/文生图/Qwen_image2.1文生图简洁版｜少参数低门槛快速上手｜新手直接抄_2104435416811261954.json、图片生成/文生图/qwen image2.1文生图利器｜数字人海报制作一步搞定_2104529003418836993.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ResolutionSelector` —— 10/12 个有
- `孤海注释` —— 9/12 个有
- `SaveImageAdvanced` —— 7/12 个有
- `QwenImage21Cache` —— 4/12 个有
- `Seed (rgthree)` —— 4/12 个有
- `ShowText|pysssss` —— 4/12 个有
- `EmptyImage` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `Anything Everywhere3` —— 2/12 个有
- `ComfySwitchNode` —— 2/12 个有
- `QwenPERewriteT8` —— 2/12 个有
- `RHLLMChatNode` —— 2/12 个有
- `Text Multiline` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
