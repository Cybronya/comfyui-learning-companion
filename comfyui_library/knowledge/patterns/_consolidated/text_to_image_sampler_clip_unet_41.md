---
name: text_to_image_sampler_clip_unet_41
type: Text To Image
frequency: 13
level: moderate
coverage: 0.944154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/xingtong_base_v2_2061416410592669697.json, 图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json, 图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json, 图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070527633288421378.json, 图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070744860063256578.json, "图片生成/文生图/图图的碧蓝幻想风格 Anima 工作流_Tutu's Blue Fantasy Style Anima workflow_2070439368904503298.json", "图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json", "图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json", "图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json", 图片生成/文生图/文生图-rh-Z-image-超清_2013965047239806978.json, 图片生成/文生图/文生图-人物_2111999328125542402.json, 图片生成/文生图/文生图-百度-ERNIE-Image_2044556450948714498.json, 图片生成/文生图/文生图ZIT_2025848646826205185.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/xingtong_base_v2_2061416410592669697.json、图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json、图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json、图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070527633288421378.json、图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070744860063256578.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `ModelSamplingAuraFlow` —— 3/13 个有
- `CLIPSetLastLayer` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `Text Multiline` —— 1/13 个有
- `easy anythingIndexSwitch` —— 1/13 个有
- `easy float` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1280 | 13 | 88% |
| 高度 | 1520 | 1024 - 1920 | 13 | 84% |
| 采样步数 | 45 | 6 - 50 | 13 | 43% |
| Prompt 约束强度(CFG) | 4 | 1 - 5 | 13 | 61% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1280，13 个样本，取值集中（一致性 88%）
- 高度 中位数 1520，观测区间 1024 - 1920，13 个样本，取值集中（一致性 84%）
- 采样步数 中位数 45，观测区间 6 - 50，13 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
