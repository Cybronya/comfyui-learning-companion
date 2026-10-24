---
name: unknown_workflow_video_lora_sampler_311
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.989
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 图生视频-极速版_1950032039593558017.json, 视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json, 视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json, 视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json, 视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json, 视频生成/图生视频/角色Lora训练素材生成_1963220175883571201.json, 视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_311

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 图生视频-极速版_1950032039593558017.json、视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json、视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json、视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json、视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 4/7 个有
- `easy int` —— 4/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `ImageResize+` —— 2/7 个有
- `ImpactInt` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `Seed Generator` —— 2/7 个有
- `CLIPVisionEncode` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 71% |
| Prompt 约束强度(CFG) | 12 | 6 - 14 | 7 | 74% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | lcm | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 14，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
