---
name: text_to_image_sampler_clip_unet_41
type: Text To Image
frequency: 10
level: moderate
coverage: 0.948
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FinePorn_Krea2基础工作流V3_2098728252046135298.json, 图片生成/文生图/KOOK_Zimage_底膜直出_2016539613388607489.json, 图片生成/文生图/Krea2 快速生图_2082367532186554370.json, 图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫场景_2085270687903731714.json, 图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫风格_2084650330515660801.json, 图片生成/文生图/Krea2_T2I_noLora_2089078237040308226.json, 图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json, 图片生成/文生图/Z-image 超清快速文生图_2008571327392784386.json, 图片生成/文生图/Zimage-ART文生图_2017256373024722946.json, 图片生成/文生图/（贞贞版）Z image Art文生图_2017605115783421953.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/FinePorn_Krea2基础工作流V3_2098728252046135298.json、图片生成/文生图/KOOK_Zimage_底膜直出_2016539613388607489.json、图片生成/文生图/Krea2 快速生图_2082367532186554370.json、图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫场景_2085270687903731714.json、图片生成/文生图/Krea2-turbo文生图赛璐璐平涂动漫风格_2084650330515660801.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/10 个有
- `PrimitiveInt` —— 2/10 个有
- `HFEPostProcessor (lrzjason)` —— 1/10 个有
- `LatentSwitch` —— 1/10 个有
- `Power Lora Loader (rgthree)` —— 1/10 个有
- `easy positive` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 30 | 10 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 34% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1080 | 720 - 1920 | 10 | 71% |
| 高度 | 1728 | 1080 - 1920 | 10 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 30，10 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1920，10 个样本
- 高度 中位数 1728，观测区间 1080 - 1920，10 个样本
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
