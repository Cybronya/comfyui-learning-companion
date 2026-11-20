---
name: unknown_workflow_sampler_clip_unet_235
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9715
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json, 图片生成/文生图/wan2.2文生图工作流_1953829480836026370.json, 图片生成/文生图/万相2.2 高质量文生图工作流_1950184764194119681.json, 视频生成/文生视频/WAN14B-文生视频_1949853875865042945.json, 视频生成/文生视频/万相 Wan2.2 14B文生视频工作流_1949831170026594305.json, 视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_235

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json、图片生成/文生图/wan2.2文生图工作流_1953829480836026370.json、图片生成/文生图/万相2.2 高质量文生图工作流_1950184764194119681.json、视频生成/文生视频/WAN14B-文生视频_1949853875865042945.json、视频生成/文生视频/万相 Wan2.2 14B文生视频工作流_1949831170026594305.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/6 个有
- `CR Text` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `JWInteger` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `LoadLatent` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 20 | 8 - 20 | 6 | 73% |
| 采样算法 | 3.5 | 1 - 3.5 | 6 | 56% |
| 调度器 | euler | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 20，观测区间 8 - 20，6 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，6 个样本
- 调度器 最常用 euler，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
