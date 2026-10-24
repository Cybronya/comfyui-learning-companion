---
name: unknown_workflow_clip_unet_vae_11
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.972875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1956141417343143938.json, 图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1957735710319112194.json, 图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1958426008351358977.json, 图片生成/文生图/Wan2.2文生图片 真实摄影  细腻皮肤质感_1960618336759480321.json, 图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json, 图片生成/文生图/wan2.2文生图工作流_1953829480836026370.json, 视频生成/文生视频/最强文生视频 wan2.2_1952267409933717505.json, 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1956141417343143938.json、图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1957735710319112194.json、图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1958426008351358977.json、图片生成/文生图/Wan2.2文生图片 真实摄影  细腻皮肤质感_1960618336759480321.json、图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PathchSageAttentionKJ` —— 7/8 个有
- `Text` —— 7/8 个有
- `SaveImage` —— 6/8 个有
- `GetImageRangeFromBatch` —— 5/8 个有
- `Wan_video_prompt_generator` —— 5/8 个有
- `easy int` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `VHS_VideoCombine` —— 2/8 个有
- `easy seed` —— 2/8 个有
- `WanMoeKSampler` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 88% |
| Prompt 约束强度(CFG) | 14 | 8 - 20 | 8 | 73% |
| 采样算法 | 3.5 | 1 - 3.5 | 8 | 62% |
| 调度器 | euler | - | 8 | 75% |
| 重绘幅度 | simple | - | 8 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 14，观测区间 8 - 20，8 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，8 个样本
- 调度器 最常用 euler，8 个样本，一致性 75%
- 重绘幅度 最常用 simple，8 个样本，一致性 88%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
