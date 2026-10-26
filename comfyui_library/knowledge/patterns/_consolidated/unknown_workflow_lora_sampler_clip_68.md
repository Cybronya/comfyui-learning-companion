---
name: unknown_workflow_lora_sampler_clip_68
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.636857
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890.json, 视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json, 视频生成/图生视频/Wan2.2 14B图生视频_2053342015286460418.json, 视频生成/图生视频/wan2.2图生视频_2067963714497765378.json, 视频生成/图生视频/wan2.2图生视频工作流-官方版_2060327159524323330.json, 视频生成/文生视频/Wan2.2 14B文生视频_2053351928163258369.json, 视频生成/文生视频/wan2.2图生视频工作流_2034905327635795970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图生视频（解禁模型）：Wan2.2_Remix_2052630486182309890.json、视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json、视频生成/图生视频/Wan2.2 14B图生视频_2053342015286460418.json、视频生成/图生视频/wan2.2图生视频_2067963714497765378.json、视频生成/图生视频/wan2.2图生视频工作流-官方版_2060327159524323330.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `WanImageToVideo` —— 6/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `ResizeImagesByLongerEdge` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 4 | 4 - 15 | 7 | 31% |
| 采样算法 | 1 | 1 - 2 | 7 | 69% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 15，7 个样本，取值分散，一致性仅 31%
- 采样算法 中位数 1，观测区间 1 - 2，7 个样本
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
