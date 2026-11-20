---
name: text_to_image_lora_sampler_clip_488
type: Text To Image
frequency: 4
level: strong
coverage: 0.87525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图片自动生成视频脚本｜图生视频角色表演脚本不用愁_2114295476941049857.json, 视频生成/图生视频/图生视频工作流｜可灵3.0 Pro多镜头最长十五秒_2100838268672757761.json, 视频生成/图生视频/图生视频首尾帧RH MiniMax-H3-Max-Turbo极速版｜锁定首尾流畅过渡_2101918968226340866.json, 视频生成/图生视频/旗舰模型图片动起来｜H3 MAX图生视频工作流_2095861857969074178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_488

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/图片自动生成视频脚本｜图生视频角色表演脚本不用愁_2114295476941049857.json、视频生成/图生视频/图生视频工作流｜可灵3.0 Pro多镜头最长十五秒_2100838268672757761.json、视频生成/图生视频/图生视频首尾帧RH MiniMax-H3-Max-Turbo极速版｜锁定首尾流畅过渡_2101918968226340866.json、视频生成/图生视频/旗舰模型图片动起来｜H3 MAX图生视频工作流_2095861857969074178.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LoadImage` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `RH_KlingV30ProImageToVideo` —— 1/4 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 1/4 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy saveText` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
