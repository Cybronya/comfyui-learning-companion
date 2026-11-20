---
name: unknown_workflow_video_clip_unet_18
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9075
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, Int, JWInteger, LoadImage, MathExpression|pysssss, ModelSamplingSD3, RH_Translator, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频官方工作流_1949895906540830722.json, 视频生成/文生视频/Wan2.2 TI2V 5B 混合版本官方工作流_1949912801272840193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频官方工作流_1949895906540830722.json、视频生成/文生视频/Wan2.2 TI2V 5B 混合版本官方工作流_1949912801272840193.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `RH_Translator`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `Wan22ImageToVideoLatent` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 12.5 | - | 2 | 40% |
| 采样算法 | 3.5 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 12.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
