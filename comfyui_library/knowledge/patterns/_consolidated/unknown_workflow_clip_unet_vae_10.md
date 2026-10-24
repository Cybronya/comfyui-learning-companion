---
name: unknown_workflow_clip_unet_vae_10
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.84125
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, ImpactInt, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2 单模低噪写实文生图_1950729804771430402.json, 图片生成/文生图/Wan2.2 最强最写实去AI感文生图_1958332452488024065.json, 图片生成/文生图/Wan2.2文生图高低噪横向测评-V2版_1950107467746295810.json, 图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json, 图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json, 图片生成/文生图/Wan最强文生图写实工作流_1948706172485414914.json, 图片生成/文生图/wan2.2高低频双采样文生图工作流（自动提示词）V3_1950782044102119425.json, 图片生成/文生图/文生图（高质量真人美女）_2035426534319722498.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Wan2.2 单模低噪写实文生图_1950729804771430402.json、图片生成/文生图/Wan2.2 最强最写实去AI感文生图_1958332452488024065.json、图片生成/文生图/Wan2.2文生图高低噪横向测评-V2版_1950107467746295810.json、图片生成/文生图/Wan2.2终极写实文生图双噪流-最新稳定版-测1920x1080_1950856807457685505.json、图片生成/文生图/Wan2.2终极写实文生图双噪流_1950564507682787330.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 6/8 个有
- `KSamplerAdvanced` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `ModelSamplingSD3` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `KSampler` —— 4/8 个有
- `LoraLoader` —— 3/8 个有
- `LoadImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `CR Simple Image Compare` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `Wan_video_prompt_generator` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| LoRA 文本强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 5.5 | 1 - 10 | 8 | 18% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | bong_tangent | - | 8 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 5.5，观测区间 1 - 10，8 个样本，取值分散，一致性仅 18%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 bong_tangent，8 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
