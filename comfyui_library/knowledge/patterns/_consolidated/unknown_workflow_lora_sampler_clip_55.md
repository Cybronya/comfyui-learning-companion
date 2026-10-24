---
name: unknown_workflow_lora_sampler_clip_55
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.931857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json, 图片生成/文生图/Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json, 图片生成/文生图/[🛫书墨]wan2_2lightning加速lora__10秒_1952444989798330370.json, 视频生成/文生视频/wan-alpha透明视频素材制作_1978258359084310529.json, 视频生成/文生视频/wan-alpha透明视频素材制作_1978685377798098945.json, 视频生成/文生视频/wan_alpha_t2v_14B透明视频wan alpha透明通道视频，让视频素材拥有无限可能，S_1979855577771839489.json, 视频生成/文生视频/小工具 wan-alpha透明图层_1973643031427551234.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json、图片生成/文生图/Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json、图片生成/文生图/[🛫书墨]wan2_2lightning加速lora__10秒_1952444989798330370.json、视频生成/文生视频/wan-alpha透明视频素材制作_1978258359084310529.json、视频生成/文生视频/wan-alpha透明视频素材制作_1978685377798098945.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `ImageToMask` —— 5/7 个有
- `InvertMask` —— 5/7 个有
- `JoinImageWithAlpha` —— 5/7 个有
- `SaveVideoRGBA` —— 4/7 个有
- `PreviewImage` —— 2/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `MaskPreview+` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SaveAnimatedWEBP` —— 1/7 个有
- `WanVideoNAG` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 7 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 7 | 0% |
| 采样算法 | uni_pc | - | 7 | 57% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，7 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 uni_pc，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
