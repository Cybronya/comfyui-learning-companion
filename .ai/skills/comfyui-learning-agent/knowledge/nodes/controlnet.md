---
name: controlnet
title: ControlNet 节点（构图控制）
category: nodes
tags: [controlnet, pose, depth, canny, union]
updated: 2026-10-04
---

# ControlNet 节点（构图控制）

## 作用
用一张参考图（边缘/深度/姿态等特征）去"牵引"采样过程，
让出图遵循指定的构图、轮廓或动作——不改变模型本身权重。

## 所属插件
**ComfyUI 内置**（节点）；ControlNet 模型文件本体来自社区，放 models/controlnet/。

## 家族成员

| 节点 | 作用 |
|---|---|
| `ControlNetLoader` | 加载 models/controlnet 下的模型 |
| `ControlNetApply` | 旧版：只接 positive，输出单条 conditioning |
| `ControlNetApplyAdvanced`（新名 `ControlNetApply`） | **推荐**：positive + negative 双接双出，`start_percent / end_percent` 控制生效区间 |
| `SetUnionControlNetType` | 给 union 型 ControlNet 指定具体控制类型（canny/depth/pose…） |
| `ControlNetInpaintingAliMamaApply` | inpaint 专用变体，带 vae 输入 |

## 关键参数

| 参数 | 说明 |
|---|---|
| `strength` | 控制强度 0–2；<1 松弛自然，>1 强制贴合（易脏脸） |
| `start_percent` | 从总步数的百分比处开始生效（如 0 = 全程） |
| `end_percent` | 结束位置；常用 0.6–0.9，后期放开让模型细化质感 |
| `control_net` | 模型本体；SD1.5 / SDXL / FLUX 模型不可混用代际 |

## 使用要点
- 链路：`preprocess 节点`（如 Canny/DWPose 估计图）→ ControlNetApply → KSampler。
- 多 ControlNet 可以**串联**（apply 输出再进下一个 apply），一个管构图一个管细节。
- Advanced 版的输出要**分别**接回 KSampler 的 positive 和 negative，接错顺序=负条件被强化。
- Union 模型（如 flux union pro）一个文件覆盖多种控制，配合 SetUnionControlNetType 用。

## 常见坑
- 预处理图与控制类型不匹配（拿深度图用 canny 模型）效果极差。
- 视频工作流里 ControlNet 通常逐帧处理，显存翻倍，注意帧数。
- strength 大 + end_percent=1.0 几乎必糊脸，先降 strength 再降区间。

## 关联卡片
- `nodes/sampler.md`（conditioning 消费端）
- `concepts/diffusion.md`（conditioning 注入位置原理）
