---
name: text_to_image_sampler_clip_unet_20
type: Text To Image
frequency: 17
level: moderate
coverage: 0.958647
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json, 图片生成/文生图/Zimage基础文生图工作流-入门学习版_2079907512651964418.json, 图片生成/文生图/anima 正式版文生图_2057111768463405058.json, 图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json, 图片生成/文生图/anima文生图基础工作流_2057116788260954114.json, 图片生成/文生图/pipi-anima-普通采样器基础文生图工作流_2064683171064672258.json, 图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json, 图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070527633288421378.json, 图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070744860063256578.json, "图片生成/文生图/图图的碧蓝幻想风格 Anima 工作流_Tutu's Blue Fantasy Style Anima workflow_2070439368904503298.json", "图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json", "图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json", "图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json", 图片生成/文生图/文生图-rh-Z-image-超清_2013965047239806978.json, 图片生成/文生图/文生图-百度-ERNIE-Image_2044556450948714498.json, 图片生成/文生图/文生图ZIT_2025848646826205185.json, 图片生成/文生图/（贞贞版）boogu满血版文生图V1_2072037602269687810.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_20

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json、图片生成/文生图/Zimage基础文生图工作流-入门学习版_2079907512651964418.json、图片生成/文生图/anima 正式版文生图_2057111768463405058.json、图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json、图片生成/文生图/anima文生图基础工作流_2057116788260954114.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 16/17 个有
- `LoraLoaderModelOnly` —— 16/17 个有
- `CR Prompt Text` —— 2/17 个有
- `CLIPLoaderGGUF` —— 1/17 个有
- `CLIPSetLastLayer` —— 1/17 个有
- `ConcatTextOfUtils` —— 1/17 个有
- `DyPE_FLUX` —— 1/17 个有
- `ShowText` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 800 - 2560 | 17 | 64% |
| 高度 | 1520 | 1024 - 1536 | 17 | 85% |
| 采样步数 | 30 | 6 - 50 | 17 | 45% |
| Prompt 约束强度(CFG) | 4 | 1 - 6.5 | 17 | 62% |
| 采样算法 | er_sde | - | 17 | 59% |
| 调度器 | simple | - | 17 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 800 - 2560，17 个样本
- 高度 中位数 1520，观测区间 1024 - 1536，17 个样本，取值集中（一致性 85%）
- 采样步数 中位数 30，观测区间 6 - 50，17 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 6.5，17 个样本
- 采样算法 最常用 er_sde，17 个样本，一致性 59%
- 调度器 最常用 simple，17 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
