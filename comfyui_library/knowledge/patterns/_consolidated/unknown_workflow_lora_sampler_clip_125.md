---
name: unknown_workflow_lora_sampler_clip_125
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.909167
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json, 视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1996850315431485442.json, 视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1_1956358088464977921.json, 视频生成/图生视频/【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json, 视频生成/文生视频/Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961.json, 视频生成/文生视频/【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/(头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json、视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1996850315431485442.json、视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1_1956358088464977921.json、视频生成/图生视频/【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json、视频生成/文生视频/Wan2.2 dyno高噪文生视频极速版V2（官方版）_1974800997673512961.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `WanFunInpaintToVideo` —— 4/6 个有
- `ImageConcanate` —— 3/6 个有
- `PDIMAGE_LongerSize` —— 3/6 个有
- `EmptyHunyuanLatentVideo` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
