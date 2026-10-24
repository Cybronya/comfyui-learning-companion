---
name: unknown_workflow_sampler_clip_unet_183
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.923286
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json, 图片生成/文生图/WAN2.2文生图_1953166220825718786.json, 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json, 图片生成/文生图/写实加强版Wan2.2文生图工作流_1956995525369323522.json, 图片生成/文生图/数字CG风格，UES渲染，超广角构图，充满神秘感且细节繁复的云雾缭绕（文生图学员练习版）+全节点注释_2046180250597466114.json, 视频生成/图生视频/wan2.2-5B图生视频女人飞走_1951274276659867650.json, 视频生成/图生视频/wan2.2-ti2v-5B文生视频摆尾猫_1952539360614920193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_183

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json、图片生成/文生图/WAN2.2文生图_1953166220825718786.json、图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json、图片生成/文生图/写实加强版Wan2.2文生图工作流_1956995525369323522.json、图片生成/文生图/数字CG风格，UES渲染，超广角构图，充满神秘感且细节繁复的云雾缭绕（文生图学员练习版）+全节点注释_2046180250597466114.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `SaveImage` —— 5/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `Wan22ImageToVideoLatent` —— 4/7 个有
- `EmptySD3LatentImage` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PreviewImage` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 30 | 7 | 54% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 7 | 52% |
| 采样算法 | uni_pc | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，7 个样本
- 采样算法 最常用 uni_pc，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
