---
name: unknown_workflow_video_sampler_clip_136
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9172
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2极速4步图生视频_1963965754733416450.json, 视频生成/图生视频/万相 Wan2.2  sage+lightx2V加速 图生视频_1949865527068024834.json, 视频生成/图生视频/图生视频 Aiwood wan2.2+2.1二阶_2033358933443747841.json, 视频生成/图生视频/图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json, 视频生成/图生视频/图生视频法阵+狂风特效工作流_2055627357901336578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan2.2极速4步图生视频_1963965754733416450.json、视频生成/图生视频/万相 Wan2.2  sage+lightx2V加速 图生视频_1949865527068024834.json、视频生成/图生视频/图生视频 Aiwood wan2.2+2.1二阶_2033358933443747841.json、视频生成/图生视频/图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json、视频生成/图生视频/图生视频法阵+狂风特效工作流_2055627357901336578.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `RIFE VFI` —— 2/5 个有
- `CreateVideo` —— 1/5 个有
- `FlashVSRNode` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `Power Lora Loader (rgthree)` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 5 | 62% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 33% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，5 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
