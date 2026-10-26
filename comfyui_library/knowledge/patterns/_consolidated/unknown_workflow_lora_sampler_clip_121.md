---
name: unknown_workflow_lora_sampler_clip_121
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9014
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, CreateVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, SimpleMath+, TextBox, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json, 视频生成/图生视频/wan2.2-加速lora-4步极速-官方-图生视频-输入主题-自动优化提示词_1956316164643323905.json, 视频生成/文生视频/wan2.2-文生视频-KJ加速版-输入大纲-自动优化提示词_1955139127446573057.json, 视频生成/文生视频/wan2.2-文生视频-火焰人_1955297362048684033.json, 视频生成/文生视频/wan2_2.14B_提示词自动优化-文生视频-加速版-KJ模型_1950557928396935169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json、视频生成/图生视频/wan2.2-加速lora-4步极速-官方-图生视频-输入主题-自动优化提示词_1956316164643323905.json、视频生成/文生视频/wan2.2-文生视频-KJ加速版-输入大纲-自动优化提示词_1955139127446573057.json、视频生成/文生视频/wan2.2-文生视频-火焰人_1955297362048684033.json、视频生成/文生视频/wan2_2.14B_提示词自动优化-文生视频-加速版-KJ模型_1950557928396935169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `SimpleMath+`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 4/5 个有
- `RH_Prompter` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `ImpactInt` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有
- `easy ifElse` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 10 | 4 - 20 | 5 | 39% |
| 采样算法 | 3.5 | 1 - 3.5 | 5 | 51% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 20，5 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，5 个样本
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
