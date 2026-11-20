---
name: unknown_workflow_sampler_clip_checkpoint_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.894
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSamplerAdvanced, OpenposePreprocessor, SDXLPromptStyler, SDXLResolutionPresets, SaveImage, Seed (rgthree), VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041.json, 平台全量/人物pose_1778054694342561793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041.json、平台全量/人物pose_1778054694342561793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `OpenposePreprocessor`
- `SDXLPromptStyler`
- `SDXLResolutionPresets`
- `SaveImage`
- `Seed (rgthree)`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 1/2 个有
- `FreeU_V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Textbox` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1.3 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | sgm_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
