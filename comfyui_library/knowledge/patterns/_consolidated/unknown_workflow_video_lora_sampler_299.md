---
name: unknown_workflow_video_lora_sampler_299
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.791286
common_nodes: [BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, ImageConcatMulti, ImageFromBatch, KSamplerAdvanced, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, RHLLMChatNode, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy imageScaleDownToSize]
problems: []
missing: []
members: [视频生成/图生视频/Bernini贝尔尼尼高噪无加速版_2061860532604465153.json, 视频生成/图生视频/Bernini贝尔尼尼高噪无加速版（超牛动作迁移）_2062715583887663106.json, 视频生成/图生视频/服装新玩法-Bernini人物替换_2020633781832519681.json, 视频生成/图生视频/服装模特视频背景替换_2065039973153333250.json, 视频生成/图生视频/高噪无加速版_2062714987814146049.json, 视频生成/文生视频/Bernini-R 主体替换视频编辑流程_2062503702258348033.json, 视频生成/文生视频/Bernini-R 参考背景视频替换流程_2062503708742733826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_299

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Bernini贝尔尼尼高噪无加速版_2061860532604465153.json、视频生成/图生视频/Bernini贝尔尼尼高噪无加速版（超牛动作迁移）_2062715583887663106.json、视频生成/图生视频/服装新玩法-Bernini人物替换_2020633781832519681.json、视频生成/图生视频/服装模特视频背景替换_2065039973153333250.json、视频生成/图生视频/高噪无加速版_2062714987814146049.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchImagesNode`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `ImageConcatMulti`
- `ImageFromBatch`
- `KSamplerAdvanced`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `RHLLMChatNode`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/7 个有
- `StringReplace` —— 4/7 个有
- `Text` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `image_scale_pixel_v2` —— 4/7 个有
- `Int` —— 3/7 个有
- `SimpleMath+` —— 2/7 个有
- `SaveImage` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 14 | 14 - 14 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 14，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
