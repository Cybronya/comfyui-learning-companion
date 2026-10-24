---
name: unknown_workflow_video_lora_sampler_473
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageConcatMulti, ImageScaleBy, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/04-09-01-WAN2.2-FMLF-首尾帧+中间帧-原生_1990969601058086914.json, 视频生成/图生视频/Wan2.2 首中尾帧-图生视频_1997905673037971457.json, 视频生成/图生视频/Wan2.2 首尾帧+中间帧_1986208144172994561.json, 视频生成/图生视频/夜魔佬首尾帧+中间帧_1982334863921561601.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_473

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/04-09-01-WAN2.2-FMLF-首尾帧+中间帧-原生_1990969601058086914.json、视频生成/图生视频/Wan2.2 首中尾帧-图生视频_1997905673037971457.json、视频生成/图生视频/Wan2.2 首尾帧+中间帧_1986208144172994561.json、视频生成/图生视频/夜魔佬首尾帧+中间帧_1982334863921561601.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `WanFourFrameReferenceUltimate` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
