---
name: text_to_image_sampler_clip_checkpoint_5
type: Text To Image
frequency: 11
level: moderate
coverage: 0.930182
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [CFG值较高可能导致Prompt约束过强]
missing: [ImageResize+]
members: [图片生成/文生图/1934989569676746753.json, 图片生成/文生图/1959857918407553025.json, 图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json, 图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json, 图片生成/文生图/冰雕世界_1792766439749373954.json, 图片生成/文生图/半透明膨胀沙发_1795724323667951617.json, 图片生成/文生图/图像增加细节和高清放大_1896189706760028161.json, 图片生成/文生图/小猫_1897084644569849857.json, 视频生成/文生视频/1792516752509292545.json, 视频生成/文生视频/高清产品摄影水果视频制作_1782313135814782978.json, 视频生成/文生视频/1782653285233111041.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1934989569676746753.json、图片生成/文生图/1959857918407553025.json、图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json、图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json、图片生成/文生图/冰雕世界_1792766439749373954.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 10/11 个有
- `UpscaleModelLoader` —— 10/11 个有
- `LoraLoader` —— 7/11 个有
- `VAEEncode` —— 6/11 个有
- `PreviewImage` —— 5/11 个有
- `ImageOnlyCheckpointLoader` —— 3/11 个有
- `ImageResize+` —— 3/11 个有
- `LatentUpscaleBy` —— 3/11 个有
- `SVD_img2vid_Conditioning` —— 3/11 个有
- `UltimateSDUpscale` —— 3/11 个有
- `VAELoader` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `VideoLinearCFGGuidance` —— 3/11 个有
- `CLIPSetLastLayer` —— 2/11 个有
- `ImageScale` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | 512 - 1024 | 11 | 77% |
| 高度 | 768 | 512 - 1280 | 11 | 70% |
| 采样步数 | 20 | 12 - 50 | 11 | 58% |
| Prompt 约束强度(CFG) | 8 | 2.5 - 48.58 | 11 | 0% |
| 采样算法 | dpmpp_2m_sde | - | 11 | 36% |
| 调度器 | normal | - | 11 | 64% |
| 重绘幅度 | 1 | 0.4 - 1 | 11 | 69% |
| LoRA 模型强度 | 0.65 | 0.55 - 1 | 7 | 74% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| CFG值较高可能导致Prompt约束过强 | 1/11 | medium | CFG值较高，可能导致Prompt约束过强 → 建议尝试CFG 7-10 |

## 建议与风险

- 宽度 中位数 640，观测区间 512 - 1024，11 个样本
- 高度 中位数 768，观测区间 512 - 1280，11 个样本
- 采样步数 中位数 20，观测区间 12 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 2.5 - 48.58，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m_sde，11 个样本，一致性 36%
- 调度器 最常用 normal，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，11 个样本
- LoRA 模型强度 中位数 0.65，观测区间 0.55 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 48.58，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：ImageResize+
