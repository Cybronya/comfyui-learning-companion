---
name: unknown_workflow_video_lora_sampler_298
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.975286
common_nodes: [CLIPLoader, CLIPTextEncode, CreateCFGScheduleFloatList, EmptySD3LatentImage, ImageResize+, Int, KSampler, LoadWanVideoT5TextEncoder, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/API-Z_image+Wan2.2_2066868599926644737.json, 视频生成/文生视频/API - Qwenimage文生图-图片组合视频_2066915773356003329.json, 视频生成/文生视频/API-Z_image+Wan2.2_2058887604485058562.json, 视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json, 视频生成/文生视频/竖屏1111_2063507047836119042.json, 视频生成/文生视频/竖屏1111_2064656978898669569.json, 视频生成/文生视频/竖屏高清_2063068057895002114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_298

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/API-Z_image+Wan2.2_2066868599926644737.json、视频生成/文生视频/API - Qwenimage文生图-图片组合视频_2066915773356003329.json、视频生成/文生视频/API-Z_image+Wan2.2_2058887604485058562.json、视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json、视频生成/文生视频/竖屏1111_2063507047836119042.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateCFGScheduleFloatList`
- `EmptySD3LatentImage`
- `ImageResize+`
- `Int`
- `KSampler`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 6/7 个有
- `LoraLoader` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `Text _O` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 7 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，7 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
