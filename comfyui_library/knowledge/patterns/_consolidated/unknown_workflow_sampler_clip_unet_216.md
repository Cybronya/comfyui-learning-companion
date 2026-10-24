---
name: unknown_workflow_sampler_clip_unet_216
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8625
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LoadImage, MaraScottIsEmptyOrNone_v1, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/文生图-Z-image-base-参考图_2039220224758648833.json, 图片生成/文生图/Z-image_-超实感文生图图返文_2026588864839688193.json, 图片生成/文生图/Z-image文生图洗图（增加图像随机性）_2000104489875013634.json, 图片生成/文生图/Z-image高清快速 文生图-_2006014329239584770.json, 图片生成/文生图/文生图-Z-image-base-参考图_2017398260050169857.json, 图片生成/文生图/文生图-Z-image-阿里造相-参考图_1993956921380192258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_216

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/文生图-Z-image-base-参考图_2039220224758648833.json、图片生成/文生图/Z-image_-超实感文生图图返文_2026588864839688193.json、图片生成/文生图/Z-image文生图洗图（增加图像随机性）_2000104489875013634.json、图片生成/文生图/Z-image高清快速 文生图-_2006014329239584770.json、图片生成/文生图/文生图-Z-image-base-参考图_2017398260050169857.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoadImage`
- `MaraScottIsEmptyOrNone_v1`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `LatentColorMatch` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `ttN concat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1024 | 6 | 85% |
| 高度 | 1280 | 1280 - 1536 | 6 | 93% |
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 10 | 10 - 30 | 6 | 43% |
| 采样算法 | 1 | 0.8 - 2.5 | 6 | 50% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1024，6 个样本，取值集中（一致性 85%）
- 高度 中位数 1280，观测区间 1280 - 1536，6 个样本，取值集中（一致性 93%）
- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 30，6 个样本，取值分散，一致性仅 43%
- 采样算法 中位数 1，观测区间 0.8 - 2.5，6 个样本，取值分散，一致性仅 50%
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
