---
name: unknown_workflow_video_clip_unet_2
type: Unknown Workflow
frequency: 16
level: weak
coverage: 0.894
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PrimitiveBoolean, RH_Captioner, SimpleMath+, TextBox, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy ifElse, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/wan2.2-14B-rapid 图生视频-最新加速模型_1950737220787458049.json, 视频生成/图生视频/wan2.2图生视频-加速工作流_1950763373552164866.json, 视频生成/图生视频/wan2.2官方图生视频，自动润色提示词_1950052256939950082.json, 视频生成/图生视频/【动态壁纸】wan2.2 视频生成工作流_1959201352268328961.json, 视频生成/图生视频/【动态海报】wan2.2 人物一致性｜图生视频_1955506935590260737.json, 视频生成/图生视频/【动态海报】wan2.2 人物一致性｜图生视频_1955507451593310209.json, 视频生成/图生视频/【最新】wan2.2 图生视频加速流_1955509045698465793.json, 视频生成/图生视频/【电影级】Wan 2.2官方图生视频｜AI 扩写提示词_1950373850129326082.json, 视频生成/图生视频/【高清】wan2.2 动态壁纸生成器｜加速_1955497249860194306.json, 视频生成/图生视频/刚开源的wan2.2-14B 官方图生视频+自动提示词_1950111733920784385.json, 视频生成/图生视频/明星海报｜Wan2.2-14B图生视频加速流_1959203655159328769.json, 视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1950878967190454273.json, 视频生成/文生视频/wan2.2-14B 官方图生视频+自动提示词_1951086042193571841.json, 视频生成/文生视频/wan2.2-14B+官方图生视频+自动提示词_1983353614280368130.json, 视频生成/文生视频/【效果炸裂】wan2.2-14B最新稳定图生视频工作流_1950410149463769089.json, 视频生成/文生视频/万相官方wan2.2图生视频_1949867321068314625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/wan2.2-14B-rapid 图生视频-最新加速模型_1950737220787458049.json、视频生成/图生视频/wan2.2图生视频-加速工作流_1950763373552164866.json、视频生成/图生视频/wan2.2官方图生视频，自动润色提示词_1950052256939950082.json、视频生成/图生视频/【动态壁纸】wan2.2 视频生成工作流_1959201352268328961.json、视频生成/图生视频/【动态海报】wan2.2 人物一致性｜图生视频_1955506935590260737.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveBoolean`
- `RH_Captioner`
- `SimpleMath+`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy ifElse`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 14/16 个有
- `CLIPVisionLoader` —— 14/16 个有
- `KSamplerAdvanced` —— 14/16 个有
- `easy cleanGpuUsed` —— 14/16 个有
- `PathchSageAttentionKJ` —— 12/16 个有
- `LayerUtility: PurgeVRAM` —— 10/16 个有
- `LayerUtility: PurgeVRAM V2` —— 6/16 个有
- `LoraLoaderModelOnly` —— 6/16 个有
- `PatchModelPatcherOrder` —— 6/16 个有
- `TorchCompileModelWanVideoV2` —— 6/16 个有
- `KSampler` —— 2/16 个有
- `Wan_video_prompt_generator` —— 2/16 个有
- `easy promptLine` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 50% |
| Prompt 约束强度(CFG) | 14 | 1 - 20 | 16 | 45% |
| 采样算法 | 3.5 | 1 - 3.5 | 14 | 49% |
| 调度器 | euler | - | 16 | 88% |
| 重绘幅度 | simple | - | 16 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 14，观测区间 1 - 20，16 个样本，取值分散，一致性仅 45%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 49%
- 调度器 最常用 euler，16 个样本，一致性 88%
- 重绘幅度 最常用 simple，16 个样本，一致性 88%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
