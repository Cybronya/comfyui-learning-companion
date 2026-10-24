---
name: unknown_workflow_sampler_clip_unet_19
type: Unknown Workflow
frequency: 26
level: weak
coverage: 0.966038
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2-live2D动态壁纸一键生成_2084626148595691521.json, 图片生成/图生图/wan2.2+lightx2v-8步图生视频-ComfyUI官方_1949980973129752578.json, 视频生成/图生视频/Wan2.2 I2V 极速图生视频 原地动作_2044755508602605570.json, 视频生成/图生视频/Wan2.2 I2V 极速版来了！Lightx2v Moe生成5秒720p视频仅需2分钟！_1978304878063804418.json, 视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json, 视频生成/图生视频/Wan2.2-live2D-动态壁纸即刻实现_2044955303057301505.json, 视频生成/图生视频/Wan2.2-live2D-动态壁纸生成_2049008127445573634.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸_2079750552161968129.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成_2077588507496894466.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成_2079019127112556545.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成_2079108169829273601.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成：可爱兔子吃夹饼_2082362157714460674.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成：旷野兔动态壁纸工作流_2082287620427706369.json, 视频生成/图生视频/Wan2.2-live2d高级可定制版-动态壁纸--可定制尺寸及时长-24fps版_2064561200037457922.json, 视频生成/图生视频/Wan2.2_图生视频4步LoRA加速-B站UP主@好奇漫步_1983147421196820482.json, 视频生成/图生视频/wan2.2+Sage加速图生视频-ComfyUI官方_1949982981533384705.json, 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1949988822005235714.json, 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1950054777926369282.json, 视频生成/图生视频/wan2.2+lightx2v-8步图生视频-ComfyUI官方（极速）_1950460812701949953.json, 视频生成/图生视频/wan2.2+lightx2v加速图生视频_1950007304294981633.json, 视频生成/图生视频/wan2.2+lightx2v加速图生视频_1954724255986544642.json, 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1949851914386194434.json, 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1950015498596564993.json, 视频生成/图生视频/wan2.2超级加速图生视频_1957799142709100545.json, 视频生成/图生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%图生视频工作流_1968502067780300801.json, 视频生成/图生视频/真男人必会韦伯斯特加钢铁侠(或其它侠)变身_1973739180855529474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/图生图/Wan2.2-live2D动态壁纸一键生成_2084626148595691521.json、图片生成/图生图/wan2.2+lightx2v-8步图生视频-ComfyUI官方_1949980973129752578.json、视频生成/图生视频/Wan2.2 I2V 极速图生视频 原地动作_2044755508602605570.json、视频生成/图生视频/Wan2.2 I2V 极速版来了！Lightx2v Moe生成5秒720p视频仅需2分钟！_1978304878063804418.json、视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 23/26 个有
- `PathchSageAttentionKJ` —— 20/26 个有
- `CFGZeroStar` —— 11/26 个有
- `ImageResizeKJv2` —— 10/26 个有
- `MathExpression|pysssss` —— 9/26 个有
- `Primitive integer [Crystools]` —— 9/26 个有
- `Text Multiline` —— 9/26 个有
- `LG_LoadImage` —— 1/26 个有
- `ModelPatchTorchSettings` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 26 | 81% |
| Prompt 约束强度(CFG) | 20 | 4 - 20 | 26 | 48% |
| 采样算法 | 3.5 | 1 - 3.5 | 26 | 49% |
| 调度器 | euler | - | 26 | 77% |
| 重绘幅度 | simple | - | 26 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，26 个样本，一致性 81%
- Prompt 约束强度(CFG) 中位数 20，观测区间 4 - 20，26 个样本，取值分散，一致性仅 48%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，26 个样本，取值分散，一致性仅 49%
- 调度器 最常用 euler，26 个样本，一致性 77%
- 重绘幅度 最常用 simple，26 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
