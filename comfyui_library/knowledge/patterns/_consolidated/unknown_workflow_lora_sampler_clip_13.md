---
name: unknown_workflow_lora_sampler_clip_13
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.782636
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950475750447173633.json, 视频生成/图生视频/2053342015286460418.json, 视频生成/图生视频/2044755508602605570.json, 视频生成/图生视频/1978304878063804418.json, 视频生成/图生视频/1983147421196820482.json, 视频生成/图生视频/1998363625523937282.json, 视频生成/图生视频/1997975012088905729.json, 视频生成/图生视频/2067963714497765378.json, 视频生成/图生视频/2060327159524323330.json, 视频生成/文生视频/Wan2.2 14B文生视频_2053351928163258369.json, 视频生成/文生视频/wan2.2图生视频工作流_2034905327635795970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1950475750447173633.json、视频生成/图生视频/2053342015286460418.json、视频生成/图生视频/2044755508602605570.json、视频生成/图生视频/1978304878063804418.json、视频生成/图生视频/1983147421196820482.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LoadImage` —— 10/11 个有
- `WanImageToVideo` —— 10/11 个有
- `ComfySwitchNode` —— 5/11 个有
- `PrimitiveBoolean` —— 5/11 个有
- `PrimitiveFloat` —— 5/11 个有
- `PrimitiveInt` —— 5/11 个有
- `ComfyMathExpression` —— 4/11 个有
- `EmptyHunyuanLatentVideo` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `ResizeImagesByLongerEdge` —— 1/11 个有
- `SetNode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 11 | 18% |
| 采样算法 | 1 | 1 - 3.5 | 11 | 43% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，11 个样本，取值分散，一致性仅 18%
- 采样算法 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 43%
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
